# AWS Lambda
In your [AWS colsole](https://aws.amazon.com/console/)
### Once you have created your Lambda function:
1. Firts, go to the API Gateway service and click on create API </br> </br>
![1](https://github.com/ga-vo/Tutorias-TelegramBot-Py-AWS/blob/master/images/Steps/1_.png)
</br>

2. Select REST API and click on Build </br> </br>
![2](https://github.com/ga-vo/Tutorias-TelegramBot-Py-AWS/blob/master/images/Steps/2.png)
</br>

3. Name your API and create it </br> </br>
![3](https://github.com/ga-vo/Tutorias-TelegramBot-Py-AWS/blob/master/images/Steps/3.png)
</br>

4. Click on Actions and Create Method  </br> </br>
![4](https://github.com/ga-vo/Tutorias-TelegramBot-Py-AWS/blob/master/images/Steps/4.png)
</br>

5. Selecti "ANY", check *Use Lambda Proxy integration* and finally, find your function and click on save</br> </br>
![5](https://github.com/ga-vo/Tutorias-TelegramBot-Py-AWS/blob/master/images/Steps/5.png)
</br>

6. Click on actions and Deploy API</br> </br>
![6](https://github.com/ga-vo/Tutorias-TelegramBot-Py-AWS/blob/master/images/Steps/6.png)\
</br>

7. Create new stage</br> </br>
![7](https://github.com/ga-vo/Tutorias-TelegramBot-Py-AWS/blob/master/images/Steps/7.png)
</br>

8. With the Invoke URL provided, visit https://api.telegram.org/bot< YOUR TOKEN>/setWebHook?url=< INVOKE URL> to set the WebHook for your bot</br> </br>
![8](https://github.com/ga-vo/Tutorias-TelegramBot-Py-AWS/blob/master/images/Steps/8.png)
