#!/usr/bin/bash

echo "start merge submit"

python3 merge_submit.py "$@"

ret=$?

if [ $ret -ne 0 ]; then
   echo "ERROR"
   exit $ret
fi

# kaggle competitions submit -c google-code-golf-2025 -f submission.zip -m "pro"

echo "done merge submit"
