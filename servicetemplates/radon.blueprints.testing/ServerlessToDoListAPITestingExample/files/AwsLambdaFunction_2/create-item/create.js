'use strict';

const AWS = require('aws-sdk');
const dynamoDb = new AWS.DynamoDB.DocumentClient();

module.exports.handler = (event, context, callback) => {
    const headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "true",
        "Content-Type": "application/json",
        "X-Requested-With": "*",
        "Access-Control-Allow-Headers": 'Content-Type,X-Amz-Date,Authorization,x-api-key,x-requested-with,Cache-Control',
    };

    const todoItem = JSON.parse(event.body);

    if (todoItem.todo === undefined) {
        return callback(null, { statusCode: 400, body: JSON.stringify("Missing or malformed 'todo' property in JSON object in request body.") });
    } else if (todoItem.todo.length < 1) {
        return callback(null, { statusCode: 400, body: JSON.stringify("Empty 'todo' property in JSON object in request body.") });
    }

    const timestamp = Math.floor(new Date() / 1000);
    const params = {
        TableName: process.env.TODOS_TABLE,
        Item: {
            id: context.awsRequestId,
            todo: todoItem.todo,
            completed: false,
            created: timestamp,
            updated: timestamp
        },
    };

    dynamoDb.put(params, (error) => {
        if (error) {
            console.log(error);
            callback(null, { headers: headers, statusCode: 400, body: JSON.stringify(error) });
        } else {
            callback(null, {
                headers: headers,
                statusCode: 200,
                body: JSON.stringify(params.Item),
            });
        }
    });

};