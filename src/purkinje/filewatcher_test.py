# -*- coding: utf-8 -*-

"""Test cases for FileWatcher"""

import gevent.monkey
gevent.monkey.patch_all()

import gevent_inotifyx as inotify
import os.path as op
import pytest
import filewatcher as sut


@pytest.fixture()
def filewatcher(tmpdir):
    """:return: FileWatcher object"""
    result = sut.FileWatcher(str(tmpdir))
    result.start()
    return result


def _test_filewatcher(fw, events):
    while True:
        event = fw.queue.get()
        events.append(event)
        print('Got inotify event: {}'.format(event))


def test_1(filewatcher):
    events = []
    g = gevent.spawn(_test_filewatcher, filewatcher, events)

    # Create a new file
    new_file_1_name = 'new_file_1.py'
    new_file_1 = op.join(filewatcher.dir, new_file_1_name)
    with open(new_file_1, 'w') as f:
        f.write('text')

    # TODO timeout might cause flaky test
    gevent.joinall([g, filewatcher.greenlet], timeout=.2)
    assert len(events) == 1
    assert events[0].name == new_file_1_name