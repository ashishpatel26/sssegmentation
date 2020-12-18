'''
Function:
    builder for different models
Author:
    Zhenchao Jin
'''
from .fcn import FCN
from .ce2p import CE2P
from .ccnet import CCNet
from .gcnet import GCNet
from .apcnet import APCNet
from .pspnet import PSPNet
from .ocrnet import OCRNet
from .dnlnet import DNLNet
from .upernet import UPerNet
from .deeplabv3 import Deeplabv3
from .nonlocalnet import NonLocalNet
from .deeplabv3plus import Deeplabv3Plus


'''build model'''
def BuildModel(cfg, mode, **kwargs):
    supported_models = {
        'fcn': FCN,
        'ce2p': CE2P,
        'ccnet': CCNet,
        'gcnet': GCNet,
        'apcnet': APCNet,
        'pspnet': PSPNet,
        'ocrnet': OCRNet,
        'dnlnet': DNLNet,
        'upernet': UPerNet,
        'deeplabv3': Deeplabv3,
        'nonlocalnet': NonLocalNet,
        'deeplabv3plus': Deeplabv3Plus,
    }
    model_type = cfg['type']
    assert model_type in supported_models, 'unsupport model_type %s...' % model_type
    return supported_models[model_type](cfg, mode=mode)