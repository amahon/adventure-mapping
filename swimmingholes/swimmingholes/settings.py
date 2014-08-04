BOT_NAME = 'swimmingholes'

SPIDER_MODULES = ['swimmingholes.spiders']
NEWSPIDER_MODULE = 'swimmingholes.spiders'

ITEM_PIPELINES = {
    'swimmingholes.pipelines.LatLonPipeline': 300,
}