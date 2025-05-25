import re
graph_log = "regex\\graph.log"

#capture_svc_node         CAPTURE1      174   582809     5036

pattern = r"\b\d+\b"

def parse_log(file_path):
    with open(file_path, "r") as graphlog:
        content = graphlog.readlines()
        for line in content:
            if "capture_svc_node" in line:
                matches = re.findall(pattern, line)
                print(matches)
                print(matches[2])
                # match = re.search(pattern,line)
                # print(match.group())

parse_log(graph_log)