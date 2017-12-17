# coding=utf-8
from __future__ import unicode_literals, absolute_import

import logging

from scrapy.exceptions import DropItem
from dynamic_scraper.models import SchedulerRuntime


class DjangoWriterPipeline:
    def process_item(self, item, spider):
        if spider.conf['DO_ACTION']:
            try:
                item['unit_page'] = spider.ref_object

                checker_rt = SchedulerRuntime(runtime_type='C')
                checker_rt.save()
                item['checker_runtime'] = checker_rt

                item.save()
                spider.action_successful = True
                dds_id_str = '{}-{}'.format(
                    str(item._dds_item_page),
                    str(item._dds_item_id)
                )
                spider.struct_log(
                    "{cs}Item {id} saved to Django DB.{ce}".format(
                        id=dds_id_str,
                        cs=spider.bcolors['OK'],
                        ce=spider.bcolors['ENDC'])
                )

            except Exception as e:
                spider.log(str(e), logging.ERROR)
                spider.log(str(item._errors), logging.ERROR)
                raise DropItem("Missing attribute.")
        else:
            if not item.is_valid():
                spider.log(str(item._errors), logging.ERROR)
                raise DropItem("Missing attribute.")
        return item
