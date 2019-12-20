import yaml
from collections import OrderedDict


# indentを維持したまま書き出すようにする
class CustomYamlDumper(yaml.Dumper):

    def increase_indent(self, flow=False, indentless=False):
        return super(CustomYamlDumper, self).increase_indent(flow, False)


def represent_odict(dumper, instance):
    return dumper.represent_mapping('tag:yaml.org,2002:map', instance.items())


# pythonインスタンスのタグを書き出さないようにする
yaml.add_representer(OrderedDict, represent_odict)

# yaml.loadをOrderedDictにして順序を維持したまま読み込むようにする
yaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, lambda loader, node: OrderedDict(loader.construct_pairs(node)))

with open('sample.yml') as f:
    data_dict = yaml.load(f)

data_dict['phases']['post_build']['commands'].append('echo hoge')

with open('out.yml', 'w') as f:
    yaml.dump(OrderedDict(data_dict), f, Dumper=CustomYamlDumper, default_flow_style=False)


