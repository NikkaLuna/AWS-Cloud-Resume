# Cloud Resume Challenge

## Overview
The Cloud Resume Project was an initiative I undertook to build and showcase my skills in cloud computing, particularly using Amazon Web Services (AWS). 

It provided a structured approach for creating a resume website hosted on AWS and gave me the opportunity to learn and implement various AWS services and best practices.

Please view the completed website here: [Cloud Resume Project](https://andreahayes-cloudresumechallenge.com)


## Features

- **Resume Website**: Built a professional resume website using HTML, CSS, and JavaScript.

- **AWS Integration**: 
  - **Amazon S3**: Hosted the static content of the website on Amazon S3, ensuring high availability and durability. S3 is used for storing HTML, CSS, JavaScript, and media files securely and efficiently.
  - **CloudFront**: Implemented Amazon CloudFront as a content delivery network (CDN) to distribute the website globally with low latency and high transfer speeds. CloudFront caches the content at edge locations around the world, improving the loading times for visitors.
  - **Route 53**: Used Amazon Route 53 for DNS management, providing reliable and cost-effective routing of end users to the website. Route 53 ensures that the website is accessible via a custom domain name, with capabilities for handling traffic and failover routing to enhance reliability.

## Deployment Automation

- **Infrastructure as Code (IaC)**: Utilized Terraform to define and provision AWS resources, including:
  - **IAM Role and Policy**: Created an IAM role and attached policies to provide the necessary permissions for the Lambda function to interact with AWS services such as DynamoDB and CloudWatch Logs.
  - **Lambda Function**: Set up a Lambda function to handle specific tasks, including the necessary handler, runtime environment, and associated permissions.
  - **Function URL**: Configured a Lambda function URL with CORS settings to allow for cross-origin requests.
  - **Deployment Package**: Used the Terraform archive provider to package the Lambda function's code for deployment.
  
- **Continuous Deployment**: Automated website deployment to an S3 bucket using a GitHub Actions workflow. This pipeline includes:
  - **Code Checkout**: Checks out the code from the repository using the `actions/checkout@master` action.
  - **S3 Synchronization**: Synchronizes the contents of the `public_html` directory with an S3 bucket using the `jakejarvis/s3-sync-action@master` action. This includes setting access control to private and enabling deletion of any removed files.



## AWS S3 Bucket Management

![AWS S3 Bucket](https://github.com/NikkaLuna/Cloud_Resume_Challenge/blob/main/S3.png)

*This screenshot shows the organization and structure of the S3 bucket used to host the resume website.*

## AWS DynamoDB Management

![AWS DynamoDB](https://github.com/NikkaLuna/Cloud_Resume_Challenge/blob/main/DynamoDB.png)

*This screenshot displays the AWS DynamoDB interface for the VisitorCount table, demonstrating the storage and retrieval of visitor counts.*


## AWS Lambda Function Management

![AWS Lambda Function](https://github.com/NikkaLuna/Cloud_Resume_Challenge/blob/main/Lambda1.png)

*This screenshot displays the AWS Lambda function VisitorCountFunction, which is integrated with an API Gateway to manage visitor counts. The Python script in the code editor handles the logic for incrementing the count in the VisitorCount DynamoDB table. This setup showcases AWS Lambda for serverless computing and real-time data processing.*


## Contributions
Contributions to the Cloud Resume Project are welcome! If you have suggestions for improvements, bug fixes, or new features, feel free to submit pull requests. Please ensure that your contributions align with the project's goals and guidelines.

## Resources
- [Official Website](https://cloudresumechallenge.dev/): Visit the official Cloud Resume Project website for detailed instructions, resources, and community support.

## License
The Cloud Resume Project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the project for personal or commercial purposes.


## Authors

- [@NikkaLuna](https://github.com/NikkaLuna)


## 🚀 About Me
I'm a Software Engineer with an emphasis on Java, Python, SQL, and AWS.  


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/andrea-hayes-msml/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/AHayes_Ninja_)
[![art portfolio](https://img.shields.io/badge/my_art-888?style=for-the-badge&logo=ko-fi&logoColor=white)](https://andreachristinehayes.wixsite.com/andreahayesart/)
