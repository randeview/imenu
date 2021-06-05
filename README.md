# imenu

Project of Software Engeneering

minikube start eval $(minkube docker-env)
docker build -t imenu:v1 . 
kubectl apply -f yaml/secret.yaml -f yaml/postgres.yaml -f yaml/deployement.yaml -f yaml/service.yaml 
kubectl delete -f yaml/secret.yaml -f yaml/postgres.yaml -f yaml/deployement.yaml -f yaml/service.yaml
helm install imenu ./imenu-chart h
elm uninstall imenu ./imenu-chart 
