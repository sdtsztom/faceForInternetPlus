from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import argparse

import cv2
import torch
import numpy as np
from glob import glob

from pysot.core.config import cfg
from pysot.models.model_builder import ModelBuilder
from pysot.tracker.tracker_builder import build_tracker

torch.set_num_threads(1)

GPUID=2

class Tracker:
    def __init__(self, config, modelPath):
        cfg.merge_from_file(config)
        cfg.CUDA = torch.cuda.is_available() and cfg.CUDA
        device = torch.device('cuda' if cfg.CUDA else 'cpu')
        self.model = ModelBuilder()
        self.model.load_state_dict(torch.load(modelPath, map_location=lambda storage, loc: storage.cpu()))
        self.model.eval().to(device)
        self.tracker = build_tracker(self.model)

    def track(self,frame,box=None):
        if box is not None:  # first Frame
            init_rect=box
            self.tracker.init(frame, init_rect)
        else:
            outputs = self.tracker.track(frame)
            if 'polygon' in outputs:
                polygon = np.array(outputs['polygon']).astype(np.int32)
                cv2.polylines(frame, [polygon.reshape((-1, 1, 2))],True, (0, 255, 0), 3)
                mask = ((outputs['mask'] > cfg.TRACK.MASK_THERSHOLD) * 255)
                mask = mask.astype(np.uint8)
                mask = np.stack([mask, mask*255, mask]).transpose(1, 2, 0)
                frame = cv2.addWeighted(frame, 0.77, mask, 0.23, -1)
            else:
                bbox = list(map(int, outputs['bbox']))
                cv2.rectangle(frame, (bbox[0], bbox[1]),(bbox[0]+bbox[2], bbox[1]+bbox[3]),(0, 255, 0), 3)
            return frame
