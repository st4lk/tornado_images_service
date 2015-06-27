Tornado images service
======================

Heroku url: [https://lit-wave-4886.herokuapp.com/](https://lit-wave-4886.herokuapp.com/)

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

- Check logs

        $ heroku logs --tail

- Test with curl (replace url if needed)

        curl -F "image=@/path/to/test.png" https://lit-wave-4886.herokuapp.com/api/images

    Also multiple files can be sent

        curl -F "image=@/path/to/test1.png" -F "image=@/path/to/test2.png" https://lit-wave-4886.herokuapp.com/api/images

- Url can be found in logs

        2015-06-27T21:30:42.021093+00:00 app[web.1]: [I 150627 21:30:42 s3:30] Amazon S3: http://bucketfortestprojects.s3.amazonaws.com/a02283b2-93d0-4007-9145-189d0f7b7e41

    So file url is [http://bucketfortestprojects.s3.amazonaws.com/a02283b2-93d0-4007-9145-189d0f7b7e41](http://bucketfortestprojects.s3.amazonaws.com/a02283b2-93d0-4007-9145-189d0f7b7e41)

Local test with curl
--------------------

- Start tornado server

        python server.py --port=8888

- Send local file to service

        curl -F "image=@/path/to/test.png" localhost:8888/api/images

- File will be saved to amazon S3, url will be logged:

        [I 150627 23:14:11 s3:30] Amazon S3: http://bucketfortestprojects.s3.amazonaws.com/10586035-02c4-467e-b0ef-8fa88fc55884
