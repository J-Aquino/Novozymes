# Novozymes
Work done for the take home assignment

To Run and install api.py (single page application api)
1). Download file
2). Ensure that you have flask installed on machine
  a). If not, navigate to python folder and execute 'pip install flask'
3). Run locally on your machine by running the following command in cmd: 'python api.py'
  a). Application will be available at: http://127.0.0.1:5000/
  
*** PLEASE NOTE: I have no experience in developing API's or experience with flask. Did the best I could with the time to at least work towards establishing the correct framework. It doesn't showcase anything other than compiling, but feel functionality is captured in the novozymes.py file. See novozymes.py for core functionality ***

Testing:
I would create different tests for the following:
- Happy Path Testing using the provided base case in the provided pdf for the assesment
- testing a blank input for genome vs filling in a value
- providing negative numbers for start and end to test edgecases (did not get to implement this logic myself)
- Use the API to find different chromosomes to input
- Use of full ATCG dna sequences
- Use of mixed ATCG and non ATCG sequences
- Use of non ATCG dna sequences

Frameworks & Libraries:
I have no experience in building API's, so whether it was django or flask, it would be the same experience for me. In terms of imports, I just took the basics of requests, json, in order to not use a full python library import to save on speed and resources.

Developer Additional Information:
- I did hardcode the initial query, you can see what I was working towards in regards to user input and parameters in my comments. 
- I noticed that my code was not handling not ATCG dna sequences, especially in regards to the reverse complement, whilst not the most elegant solution I coded in a swap. I would remedy this by putting additional logic in the for loops to handle ATCG vs non ATCG. The first to handle the non ATCG case, giving it the logic to retain it's value, in additon full non ATCG sequences should default to a 0 CG calculation.

Questions:
For initial framework, I would aim to use Amazon EC2, as it is focused on quick setup with high scalability in the cloud foregoing the need for upfront hardware. When it comes to managing the data itself using AWS, it would be best to an object based storage such as Amazon ElastiCache to focus on performance and handling user load. ElastiCache has a self healing infrastructure to ensure that services do not suffer. This method helps with less overhead in regards to scalability. From what I've read, the best database would have to be AMAZON RDS, in regards to standing it up, as well as ease of scalability.
