#!/bin/bash
ln -sf "$PWD/test.sh" .git/hooks/pre-commit

pylint next_num
rc=$?;
if [[ $rc != 0 ]];
then
    echo "Fix pylint"
    exit $rc;
fi

python -m unittest next_num_tests.py
rc=$?;
if [[ $rc != 0 ]];
then
    echo "Fix unittests"
    exit $rc;
fi

echo "Tests pass";
exit 0;
