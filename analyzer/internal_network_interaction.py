import multiprocessing
from utilities.addresses import *
from utilities.handlers import file_load
import re
#import networkx as nx


class InternalInteraction(multiprocessing.Process):
    """docstring for InternalInteraction"""

    def __init__(self, arg):
        super(InternalInteraction, self).__init__()
        self.parsed_packet = arg
        # self.graph =

    def generate_graph(self):
        """Summary

        Returns:
            TYPE: Description
        """
        pass

    def run(self):
        """Summary

        Returns:
            TYPE: Description
        """
        srcIP = extractSrcIP(self.parsed_packet)
        destIP = extractDestIP(self.parsed_packet)
        # if True:
        #generate_graph(srcIP, destIP)
        payload = getPayload(self.parsed_packet)
        # print(self.parsed_packet)
        if payload is not None:
            fingerprints = file_load(
                '/home/abhi/Downloads/CourseMaterial/Networking/Information_Security/projects/breach-detection-system/datasets/shell_commands.txt')
            #print(fingerprints)
            score = 0
            cmd_list = ""
            for command in fingerprints:
                #match_obj = re.match(command, payload['application_data'], re.M)
                if command in payload['application_data']:
                    score += 1
                    cmd_list += ", " + command
                else:
                    pass
            if score > 2:
                print("[BREACH]" + "shell commands found in payload, following commands were executed\n"
                    + cmd_list)
            return score
        else:
            return "Payload is empty"
        # else:
            # return None
