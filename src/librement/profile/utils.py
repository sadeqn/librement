# Copyright 2012 The Librement Developers
#
# See the AUTHORS file at the top-level directory of this distribution
# and at http://librement.net/copyright/
#
# This file is part of Librement. It is subject to the license terms in
# the LICENSE file found in the top-level directory of this distribution
# and at http://librement.net/license/. No part of Librement, including
# this file, may be copied, modified, propagated, or distributed except
# according to the terms contained in the LICENSE file.

import hashlib
import feedparser

from django.core.cache import cache

def get_rss_feed(url):
    if not url:
        return None

    key = 'feed:%s' % hashlib.sha1(url).hexdigest()
    feed = cache.get(key)

    if feed is None:
        feed = feedparser.parse(url)
        cache.set(key, feed, 3600)

    return feed
