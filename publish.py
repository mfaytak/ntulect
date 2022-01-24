#!/usr/bin/env python

# Convert a Markdown file to Slidy HTML format using
# Pandoc, then add bells and whistles to the output.
# Currently, adds FontAwesome CDN for easy inline text 
# icons using CSS pseudoelements without directly styling
# the HTML output of Pandoc.

# TODO automatically add audio buttons
# TODO automatically size/style YouTube iframe elements
#  define general fcn for open-insert-write
#  do this both for the header (current)
#    and every <audio> element
#  if more general, fa-head might be better stored as
#    a tab-delim file that contains all insert strings
#    and differently named

# TODO generate a paginated PDF output from Markdown

import os, argparse, subprocess
from shutil import move
from tempfile import mkstemp

parser = argparse.ArgumentParser()
parser.add_argument("infile", help="Markdown file containing lecture content")
args = parser.parse_args()

# define input and output files
infile = args.infile
if not infile.endswith(".md"):
	raise ValueError("Input must be Markdown file with .md extension")
slides = os.path.splitext(infile)[0] + ".html"

# define arguments for subprocess and run
pandoc_args = [ "pandoc",
			    "-t", "slidy",
			    "-V", "slidy-url=assets", # TODO un-hard-code slidy URL
			    "-s", infile,
			    "-o", slides
			]
ret = subprocess.Popen(pandoc_args,
	stdin = subprocess.PIPE,
    stdout = subprocess.PIPE)
ret.communicate()

# get fontawesome CDN from file
with open("fa-head.txt", 'r') as fa_head:
	fa_cdn = '\n'.join(fa_head.readlines())

# temp file
fh, abs_path = mkstemp()

# insert CDN after <head> opening tag and write to temp
with os.fdopen(fh, 'w') as new_file:
	with open(slides) as old_file:
		lines = old_file.readlines()
		new_lines = [l + fa_cdn if "<head>" in l 
			 	 	 else l for l in lines]
		new_file.write('\n'.join(new_lines))

# delete old file and replace with temp
os.remove(slides)
move(abs_path, slides)
