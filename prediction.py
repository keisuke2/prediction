#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line sample for the Google Prediction API

Command-line application that trains on your input data. This sample does
the same thing as the Hello Prediction! example. You might want to run
the setup.sh script to load the sample data to Google Storage.

Usage:
  $ python prediction.py "bucket/object" "model_id" "project_id"

You can also get help on all the command-line flags the program understands
by running:

  $ python prediction.py --help

To get detailed log output run:

  $ python prediction.py --logging_level=DEBUG
"""
from __future__ import print_function

__author__ = ('jcgregorio@google.com (Joe Gregorio), '
              'marccohen@google.com (Marc Cohen)')

import argparse
import os
import pprint
import sys
import time

from apiclient import discovery
from apiclient import sample_tools
from oauth2client import client


# Time to wait (in seconds) between successive checks of training status.
SLEEP_TIME = 10


# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument('object_name',
    help='Full Google Storage path of csv data (ex bucket/object)')
argparser.add_argument('model_id',
    help='Model Id of your choosing to name trained model')
argparser.add_argument('project_id',
    help='Model Id of your choosing to name trained model')


def print_header(line):
  '''Format and print header block sized to length of line'''
  header_str = '='
  header_line = header_str * len(line)
  print('\n' + header_line)
  print(line)
  print(header_line)


def main(argv):
  # If you previously ran this app with an earlier version of the API
  # or if you change the list of scopes below, revoke your app's permission
  # here: https://accounts.google.com/IssuedAuthSubTokens
  # Then re-run the app to re-authorize it.
  service, flags = sample_tools.init(
      argv, 'prediction', 'v1.6', __doc__, __file__, parents=[argparser],
      scope=(
          'https://www.googleapis.com/auth/prediction',
          'https://www.googleapis.com/auth/devstorage.read_only'))

  try:
    # Get access to the Prediction API.
    papi = service.trainedmodels()

    # List models.
    print_header('Fetching list of first ten models')
    result = papi.list(maxResults=10, project=flags.project_id).execute()
    print('List results:')
    pprint.pprint(result)

    # Start training request on a data set.
    print_header('Submitting model training request')
    body = {'id': flags.model_id, 'storageDataLocation': flags.object_name}
    start = papi.insert(body=body, project=flags.project_id).execute()
    print('Training results:')
    pprint.pprint(start)

    # Wait for the training to complete.
    print_header('Waiting for training to complete')
    while True:
      status = papi.get(id=flags.model_id, project=flags.project_id).execute()
      state = status['trainingStatus']
      print('Training state: ' + state)
      if state == 'DONE':
        break
      elif state == 'RUNNING':
        time.sleep(SLEEP_TIME)
        continue
      else:
        raise Exception('Training Error: ' + state)

      # Job has completed.
      print('Training completed:')
      pprint.pprint(status)
      break

    # Describe model.
    print_header('Fetching model description')
    result = papi.analyze(id=flags.model_id, project=flags.project_id).execute()
    print('Analyze results:')
    pprint.pprint(result)

    # Make some predictions using the newly trained model.
    #DBの呼び出し
    import MySQLdb
  
    if __name__ == "__main__":
  
      connector = MySQLdb.connect(host="10.0.1.75", db="jobhunt", user="jobhunt", passwd="jobhuntpasswd", charset="utf8")
      cursor = connector.cursor()
        
      sql = "select name from users"
      #sql2 = "INSERT INTO users (id, name) VALUES (5,3)"
      #sql2 ="INSERT INTO jobhunt.users (id, name) VALUES (2,2)"
      cursor.execute(sql)
      records = cursor.fetchall()
      for record in records:
          print (record[0])
      cursor.close()
      connector.close()
      #tst
      print('呼びだし完了')
    #DBの呼び出し
    import MySQLdb

    if __name__ == "__main__":

      connector = MySQLdb.connect(host="10.0.1.75", db="jobhunt", user="jobhunt", passwd="jobhuntpasswd", charset="utf8")
      cursor = connector.cursor()

      #sql = "select name from users"
      #sql = 'INSERT INTO users (id, name) VALUES (%d, %s)', (12, "keiuske")
      #sql2 ="INSERT INTO jobhunt.users (id, name) VALUES (2,2)"
      cursor.execute('insert into tests (name) values ("なぜ消えるのだ?")')
      #cursor.execute('insert into tests (name) values ("なぜ消えるのだ")')
      #cursor.execute('insert into tests (name) values (%s)', ("keisuke"))
      #cursor.execute(sql)
      # select
      cursor.execute('select * from tests')
      row = cursor.fetchone()

      # 出力
      for i in row:
        print(i)
      
      cursor.close()
      connector.commit()
      connector.close()
      #tst
      print('インサート完了')
    
    print_header('Making some predictions')
    for sample_text in [record[0]]:
      body = {'input': {'csvInstance': [sample_text]}}
      result = papi.predict(
        body=body, id=flags.model_id, project=flags.project_id).execute()
      print('Prediction results for "%s"...' % sample_text)
      pprint.pprint(result)

    if __name__ == "__main__":

      connector = MySQLdb.connect(host="10.0.1.75", db="jobhunt", user="jobhunt", passwd="jobhuntpasswd", charset="utf8")
      cursor = connector.cursor()
	
      #cursor.execute('insert into tests (name) values (result)')
      #cursor.execute('insert into tests (name) values ("なぜ消えるのだ")')
      #cursor.execute(sql)
      # select
      cursor.execute('select * from tests')
      row = cursor.fetchone()

      # 出力
      for i in row:
        print(i)

      cursor.close()
      connector.commit()
      connector.close()
      #tst
      print('インサート完了')
      ##pprint.pprint(result)
     # print (result)
      import json
      array = json.dumps(result)
      #array = json.dumps({u'label': u'true', u'score': u'0.384615'})
      #data['outputMulti']=[{u'score': u'0.384615', u'label': u'true'}, {u'score': u'0.615385', u'label': u'false'}]
      data=json.loads(array)
      #print (data['outputMulti'])      
      #from pprint import pprint as pp
      #pp(result)
      data2 = data['outputMulti']
      print(data2)
      print(data2[0]['label'])
      print(data2[0]['score'])
      evaluate = data2[0]['label']
      score = data2[0]['score']
       #DBの呼び出し
    import MySQLdb

    if __name__ == "__main__":

      connector = MySQLdb.connect(host="10.0.1.75", db="jobhunt", user="jobhunt", passwd="jobhuntpasswd", charset="utf8")
      cursor = connector.cursor()

      #sql = "select name from users"
      #sql = 'INSERT INTO users (id, name) VALUES (%d, %s)', (12, "keiuske")
      #sql2 ="INSERT INTO jobhunt.users (id, name) VALUES (2,2)"
      #cursor.execute('insert into tests (name) values (%s)',([evaluate]))
      cursor.execute('UPDATE tests SET name  = (%s) WHERE name = "なぜ消えるのだ?"',([evaluate]))
      #cursor.execute('insert into tests (name) values ("なぜ消えるのだ")')
      #cursor.execute('insert into tests (name) values (%s)', ("keisuke"))
      #cursor.execute(sql)
      # select
      cursor.execute('select * from tests')
      row = cursor.fetchone()

      # 出力
      for i in row:
        print(i)

      cursor.close()
      connector.commit()
      connector.close()
      #tst
      print('インサート完了')



    # Delete model.
    print_header('Deleting model')
    result = papi.delete(id=flags.model_id, project=flags.project_id).execute()
    print('Model deleted.')

  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run '
           'the application to re-authorize.')


if __name__ == '__main__':
  main(sys.argv)
