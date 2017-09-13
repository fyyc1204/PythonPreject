#清除filter表所有规则
iptables -F
#设定INPUT OUTPUT FORWARD的默认策略为DROP
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT DROP

#chain INPUT
iptables -A INPUT -p icmp -j ACCEPT
iptables -A INPUT -p tcp -s 192.168.41.12 --dport 22 -j ACCEPT
iptables -A INPUT -p tcp -s 192.168.41.77 --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p udp --sport 53 -j ACCEPT
#chain OUTPUT
iptables -A OUTPUT -p tcp -d 192.168.41.12 --sport 22 -j ACCEPT
iptables -A OUTPUT -p tcp -d 192.168.41.77 --sport 22 -j ACCEPT
iptables -A OUTPUT -p tcp  --sport 80 -j ACCEPT
iptables -A OUTPUT -p tcp  --dport 80 -j ACCEPT
iptables -A OUTPUT -p icmp -j ACCEPT
iptables -A OUTPUT -p udp --dport 53 -j ACCEPT


#保存iptables设定
service iptables save

#重启iptables
service iptables restart