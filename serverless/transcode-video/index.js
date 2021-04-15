'use strict';

/* Process:
 * New file uploaded to S3 triggers this lambda
 * Lambda creates a video transcode job
 * Job submitted to transcode video
 * Transcoded video saved to bucket
 * Message status to Amazon CloudWatch Log
 */
const AWS = require('aws-sdk');
const PIPELINE_ID = '1576548221495-rrr7x7';
let elasticTranscoder = new AWS.ElasticTranscoder({region: 'us-west-2'});


exports.handler = function(event, context, callback) {
  const key = event.Records[0].s3.object.key; // uniquely ids obj in bucket
  // If file is called "my bday video.mp4" url will be "my+bday+video.mp4"
  // Convert back
  const sourceKey = decodeURIComponent(key.replace(/\+/g, ' '));
  const outputKey = sourceKey.split('.')[0];
  console.log('key:', key, sourceKey, outputKey);
  const params = {PipelineId: PIPELINE_ID,
                  OutputKeyPrefix: outputKey + '/',
                  Input: {Key: sourceKey},
                  Outputs: [{Key: outputKey + '-1080p.mp4',
                             PresetId: '1351620000001-000001'},
                            {Key: outputKey + '-720p.mp4',
                             PresetId: '1351620000001-000010'},
                            {Key: outputKey + '-web-720p.mp4',
                             PresetId: '1351620000001-1000070'}]};


  elasticTranscoder.createJob(params, function(error, data) {
      // if transcoder fails, use callback to write error to CloudWatch
      if (error) { callback(error); } 
  });
};


