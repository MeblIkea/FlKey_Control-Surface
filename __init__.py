from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, REMOTE, SCRIPT, SYNC, \
    controller_id, inport, outport
from .flkey import FlKey


def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=4661,
                                              product_ids=[317],  # FIND STUFF HERE
                                              model_name=['FLkey MIDI'])),
            PORTS_KEY: [
                inport(props=[NOTES_CC, REMOTE]),
                inport(props=[NOTES_CC, SCRIPT]),
                outport(props=[SYNC, REMOTE]),
                outport(props=[NOTES_CC, SCRIPT])]}


def create_instance(c_instance):
    return FlKey(c_instance=c_instance)
