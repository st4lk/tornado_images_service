Tornado images service
======================

Upload to heroku
----------------
- Create app

        $ heroku create

- Define Amazon S3 credentials

        $ heroku config:set AWS_ACCESS_KEY=xxx AWS_SECRET_KEY=yyy

- Optional define Amazon S3 bucket name (default 'bucketfortestprojects')

        $ heroku config:set S3_BUCKET=zzz

- Push to heroku

        $ git push heroku master

Test with curl
--------------

- Start tornado server

        python server.py --port=8888

- Send local file to service

        curl -F "image=@/path/to/test.png" localhost:8888/api/images

- File will be saved to amazon S3, url will be logged:

        [I 150627 23:14:11 s3:30] Amazon S3: http://bucketfortestprojects.s3.amazonaws.com/10586035-02c4-467e-b0ef-8fa88fc55884
