# Makefile for source rpm: python-docs
# $Id$
NAME := python-docs
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
