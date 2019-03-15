#!/bin/bash
for f in *.py
do
	sed -i.bak '1,9d' $f
rm *.bak	  
done
