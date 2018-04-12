import sys
import boto3
import json

from botocore.exceptions import ClientError


class ImageCopy:
    """
    ami copy from us-west-2 to ap-northeast-1
    """

    def __init__(self, src_image_id=None):
        """
        initialize
        """
        self.src_image_id = src_image_id
        self.src_image_name = self.get_src_image_name()
        self.src_image_tags = self.get_src_image_tag()

    def get_src_image_name(self):
        """
        get source ami name
        """
        client = boto3.client('ec2', region_name='us-west-2')
        response = client.describe_images(
            ImageIds=[self.src_image_id]
        )

        return response['Images'][0]['Name']

    def get_src_image_tag(self):
        """
        get tag info of source ami
        """
        client = boto3.client('ec2', region_name='us-west-2')
        response = client.describe_images(
            ImageIds=[self.src_image_id]
        )

        return response['Images'][0]['Tags']

    def tagging_dst_image(self):
        """
        tagging destination ami
        """
        session = boto3.session.Session(region_name='ap-northeast-1')
        ec2 = session.resource('ec2')
        image = ec2.Image(self.dst_image_id)
        image.create_tags(Tags=self.src_image_tags)

    def image_copy(self):
        """
        copy ami
        """
        description = "[Copied " + self.src_image_id + " from us-west-2] " + self.src_image_name
        client = boto3.client('ec2', region_name='ap-northeast-1')
        response = client.copy_image(
            Description=description,
            Name=self.src_image_name,
            SourceImageId=self.src_image_id,
            SourceRegion='us-west-2',
        )

        self.dst_image_id = response['ImageId']
        print(json.dumps({"ImageId": self.dst_image_id}, indent=4, sort_keys=False))


if __name__ == '__main__':
    arguments = sys.argv
    if (len(arguments) != 2):
        print('Usage: # python %s source_ami_id' % arguments[0])
        quit()

    # first argument is self file name.
    script = arguments.pop(0)

    src_image_id = arguments.pop(0)

    # ami copy
    obj = ImageCopy(src_image_id)
    obj.image_copy()

    # tagging to destination ami
    obj.get_src_image_tag()
    obj.tagging_dst_image()

