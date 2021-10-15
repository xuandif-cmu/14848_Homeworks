1. Steps for getting applications working on GKE:
    1. Build and push docker images locally for sentiment-analysis-frontend, sentiment-analysis-web-app,sentiment-analysis-logic. 
        E.g. for frontend, use the following command to build and push docker images,
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
    3. Check the external IP of web-app and substitute the web-app ip in the App.js, then update the docker image for frontend,
        ```
        docker build -f Dockerfile -t xuandif/sentiment-analysis-frontend:minikube .
        docker push xuandif/sentiment-analysis-frontend:minikube
        ```
    4. Update the Kubernete container for frontend with,
        ```
        kubectl apply -f sa-frontend-deployment.yaml
        ```
        And then it's all set.
2. Screenshot for the execution of your application on Google Kubernetes Engine,
    - GKE.png: showing the external IP for frontend-app running on GKE
    - app.png: showing the application running on that external IP.
3. Docker Hub images:
    - https://hub.docker.com/r/xuandif/sentiment-analysis-frontend (use "minikube80" tag)
    - https://hub.docker.com/r/xuandif/sentiment-analysis-logic
    - https://hub.docker.com/r/xuandif/sentiment-analysis-web-app
  
4. VideoDemo:
    Please select 1080p for the following videos,
    - Youtube: https://www.youtube.com/watch?v=2W7Sx7066TI
    - In case youtube link not working, Google drive link is also provided here: https://drive.google.com/file/d/19NKc-l1LqbW42_DDchP4smkWgdnWnN0R/view?usp=sharing
