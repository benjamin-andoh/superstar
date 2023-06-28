kubectl get pv pvc, sc
kubectl get nodes -o wide
`
minikube service superstar-service --url
`

kubectl run -it --rm --image=mysql:5.6 --restart=Never mysql-client -- mysql -h mysql -u root -pdbpassword11

kubectl delete -f EKS/kube-manifest

kubectl get pods -w

Namespace
---------
kubectl get all --namespace kube-system 
kubectl create namespace dev1
kubectl create namespace dev2
kubectl apply -f Eks/kube-manifests/ -n dev1
kubectl get all -n dev1
kubectl get pvc -n dev1
kubectl get ns 
kubectl delete ns dev1
kubectl get all --all -namespaces