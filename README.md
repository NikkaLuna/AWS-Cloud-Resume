Persevering Through the Cloud Resume Challenge: My Professional Journey 

This article shares the struggles and lessons learned from manuerving through the complexities of the Cloud Resume Challenge. Professional growth results from concurring its roadblocks. 


Professionals and cloud computing enthusiasts. Welcome to The Cloud Resume Challenge. The Cloud Resume Challenge is an effort to show technical and personal growth by engaging with all aspects of AWS architectures. This is not just a case of connecting services and writing code but of the internal change when facing challenges and learning inwardly about what those areas are. In this short reflection I’m going to discuss the meat of my struggle and triumphs through-out this challenge and the professional insights I have encountered. Let us embark on this journey and explore the determination and no quit that it takes to excel in the a cloud focused field of technology.


One of my favorite projects of all time. Why? Not just because it tested my skill, and my will in Cloud Computing but I learned so much about problem solving, tenacity, and the AWS Ecosystem! What I had done here was basically build a series of technical challenges that forced me to learn every nook and cranny of the AWS platform for me to complete my goal, which at the time was to get into the CIVO Hackathon.


One of the first significant roadblocks that I hit was when I was using AWS Lambda. I was hitting CORS (Cross-Origin Resource Sharing) errors and I couldn't identify the source of it. Coming to learn that a simple typo (which happened when I wrote an import json statement the imported json library, and had an extra 'l' at the end of json. Thus, the system was unable to find this module, which caused the error (knowing AWS, I'm sure the precise error that I hit would not have clouded CORS if I didn't have a typo).


IAM policy is another place where it is necessary to pay close attention to the details. My intent was to simply allow my application to perform PutItem actions on a DynamoDB table. However, the Amazon mechanism for accomplishing this is anything other than simple. Writing the policy using JSON, making sure my policy had a correct name and attaching it to the right role called for accuracy; screwing up any of that would definitely break the security and functionality of my service. AWS CLI became instrumental to me since commands like aws lambda get-function-configuration were crucial in confirming that indeed everything was correctly configured/operational.


DNS at the CloudFront Conundrum One of the most confusing issues involved my domain name not properly linking to the AWS CloudFront distribution. The error message “We can’t connect to the server at andreahayes-cloudresumechallenge.com” plagued me. I meticulously checked my DNS Configuration in Route 53, confirmed that my CloudFront distribution was deployed and enabled correctly, yet it still would not budge. It wasn’t until I carefully reviewed EVERYTHING at around 10 p.m. one night did I find the missing piece of the puzzle. I did not have the ‘alternate domain names’ configured correctly in the CloudFront settings. So, slight oversight on my end to link your domain to the corresponding CloudFront distribution. Good to know.


Technical problems were the most frustrating part of the system because I was not familiar with some of the terms on the assignment instructions, but I looked them up and figure it out. There was a lot of trail and error when it came to the technical aspect of the program, but that is how I learn the best. To me an error in the technical aspects provided me with more knowledge. I knew what did not working with the system so I just had to figure out what did work. Technical problems were not apart of the three policy categories so I did not receive many grammar errors.


The Cloud Resume Challenge turned into much more than just completing a task. It turned into an educational journey encompassing getting a perspective in why it was so important to approach the tasks methodically, knowledge of cloud services, and unexpected challenges that even seems so apparent.


To those just joining cloud computing, I would give the advice to be patient, detail oriented and to really understand the systems, because, they aren’t so straight-forward most of the time. One thing I would suggest for people to know is that the cloud is constantly evolving and growing. As one challenge is tackled, another appears, as detail oriented as you can be, you won’t ever know everything there is to know.


It is with pride that I link this post in my resume, I must say that it is has been a truly a arduous Journey through the Cloud Resume Challenge, the professional growth and knowledge is immeasurable. For my readers, learn from my struggles, embrace the challenges, and the journey through the cloud is as enriching as mine has been.



## Authors

- [@NikkaLuna](https://github.com/NikkaLuna)


## 🚀 About Me
I'm a student developer with an emphasis on Java, C++, and Python.  


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://andreachristinehayes.wixsite.com/andreahayesart/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/andrea-hayes-msml/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/AHayes_Ninja_)
