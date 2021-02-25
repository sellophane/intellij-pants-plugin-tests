#!/usr/bin/python3
bazelproject_template_path = "ij-seed/templates/bazelproject.tpl"
workspace_template_path = "ij-seed/templates/workspace.tpl"

bazelproject_output_path = ".bazelproject"
workspace_output_path = ".idea/workspace.xml"

idea_path = "idea"

import sys, shutil, os, subprocess
from string import Template
import getopt

optlist, args = getopt.getopt(sys.argv[1:], 'l:', ["languages="])

bazel_targets = "\n  ".join(args)
bazel_languages = ""
for o, a in optlist:
    if o in ("-l", "--languages"):
        bazel_languages = "\n  ".join(a.split(','))

os.makedirs(".idea", exist_ok=True)
with open(bazelproject_template_path, "r") as t:
    bazelproject_template = Template(t.read())
bazelproject_output = bazelproject_template.substitute(BZL_TARGETS=bazel_targets, BZL_LANGUAGES=bazel_languages)
with open(bazelproject_output_path, "w") as output:
    output.write(bazelproject_output)
shutil.copyfile(workspace_template_path, workspace_output_path)

subprocess.run([idea_path, "."])