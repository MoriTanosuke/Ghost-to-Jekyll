#!/usr/bin/python
import json
import sys
import codecs
from pprint import pprint
from string import Template

def read(input_file):
	json_file = open(input_file, 'r')
	data = json.load(json_file)
	json_file.close()
	return data

def is_published(post):
	if status(post) == "published":
		return post
	else:
		return None

def is_draft(post):
	if not is_published(post):
		return post
	else:
		return None

def title(post):
	return post["title"]

def markdown(post):
	return post["markdown"]

def slug(post):
	return post["slug"]

def status(post):
	return post["status"]

def created(post):
	return post["created_at"]

def published(post):
	return post["published_at"]

def uuid(post):
	return post["uuid"]

def tag_for_post(post, tags, posts_tags):
	myId = post["id"]
#	print "Searching for " + str(myId) + " in " + str(posts_tags)
	post_tag = filter(lambda p: p["post_id"] == myId, posts_tags)
#	print "Found " + str(post_tag)
	tag_id = post_tag[0]["tag_id"]
	print "Returning tag for tag_id " + str(tag_id)
	return filter(lambda tag: tag != None, map(lambda tag: tag if tag["id"] == tag_id else None, tags))

input_file = sys.argv[1]
print "Reading data from " + input_file
data = read(input_file)

# get needed data
posts = data["db"][0]["data"]["posts"]
tags = data["db"][0]["data"]["tags"]
posts_tags = data["db"][0]["data"]["posts_tags"]

# split into published/draft
published = filter(lambda p: p != None, map(is_published, posts))
drafts = filter(lambda p: p != None, map(is_draft, posts))


### create files
#prefix = '_posts/'
prefix = ''
s = Template("""
---
title: $title
date: $published_at
---
$markdown
""")

print "Published: " + str(len(published)) + " Draft: " + str(len(drafts))

# TODO loop over published, create _posts/YYYY-MM-DD-'slug'.markdown
#for post in posts:
post = posts[0]
pprint(post)
date = str(post["published_at"])
slug = slug(post)

fpost = codecs.open(prefix + date + '-' + slug + '.markdown', 'w', 'utf-8')
fpost.write(s.substitute(post))
fpost.close()
# TODO loop over drafts, create _drafts/YYYY-MM-DD-'slug'.markdown

