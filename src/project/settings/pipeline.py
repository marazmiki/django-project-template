# coding: utf-8

from settings import MIDDLEWARE_CLASSES, rel


PIPELINE = True
PIPELINE_VERSION = False

if PIPELINE_VERSION:
    STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
else:
    STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

#PIPELINE_DISABLE_WRAPPER = True

PIPELINE_CSS = {
    'all_in_one': {
        'source_filenames': (
        ),
        'output_filename': 'css/all_in_one.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}


PIPELINE_JS = {
    'all_in_one': {
        'source_filenames': (
            'base/js/jquery-1.8.2.min.js',
            'base/js/date.js',
            'base/js/json2.js',
        ),
        'output_filename': 'js/all_in_one.js'
    }
}


PIPELINE_CSS_COMPRESSOR = None #'pipeline.compressors.yui.YUICompressor'
PIPELINE_JS_COMPRESSOR  = None #'pipeline.compressors.yui.YUICompressor'


MIDDLEWARE_CLASSES += (
    'django.middleware.gzip.GZipMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
)

