#!/usr/bin/env python2

from distutils.core import setup

setup(
    name='torrent-preview',
    version='1.0',
    author='Allen Li',
    author_email='darkfeline@felesatra.moe',
    requires=['bencode(>=1.0)'],
    url='http://felesatra.moe/',
    scripts=['torrent-preview'],
)
