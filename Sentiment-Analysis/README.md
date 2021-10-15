1. Steps for getting applications working on GKE:
    1. Build docker images for sentiment-analysis-frontend, sentiment-analysis-web-app,sentiment-analysis-logic and then push them to docker hub.
        E.g. for frontend, use the following commands to build and push docker images,
        ```
        docker build -f Dockerfile -t xuandif/sentiment-analysis-frontend .
        docker push xuandif/sentiment-analysis-frontend
        ```
    2. Create Kubernetes cluster and deploy services and containers on cluster. 
        E.g. for frontend, use the following command,
        ```
        kubectl apply -f sa-frontend-deployment.yaml
        kubectl apply -f service-sa-frontend-lb.yaml
        ```
        (Note: the name of sa-logic service is changed to sa-logic-svc to make it distinguishable with sa-logic container.)
    3. Check the external IP of web-app,
        ```
        kubectl get svc
        ```
        Substitute the web-app ip in the App.js of frontend, then update the docker image for frontend,
        docker build -f Dockerfile -t xuandif/sentiment-analysis-frontend:minikube80 .
        docker push xuandif/sentiment-analysis-frontend:minikube80
        ```
    4. Update the Kubernete container for frontend with,
        ```
        kubectl apply -f sa-frontend-deployment.yaml
        ```
        And then it's all set.
2. Screenshots for the execution of my application on Google Kubernetes Engine,
    - app.png: showing the application running on that external IP.
    - GKE.png: showing the external IP for frontend-app running on GKE
3. Docker Hub images:
    - https://hub.docker.com/r/xuandif/sentiment-analysis-frontend (use "minikube80" tag)
    - https://hub.docker.com/r/xuandif/sentiment-analysis-logic
    - https://hub.docker.com/r/xuandif/sentiment-analysis-web-app
  
4. VideoDemo:
    Please select 1080p for the following videos,
    - Youtube: https://www.youtube.com/watch?v=2W7Sx7066TI
    - In case youtube link not working, Google drive link is also provided here: https://drive.google.com/file/d/19NKc-l1LqbW42_DDchP4smkWgdnWnN0R/view?usp=sharing
