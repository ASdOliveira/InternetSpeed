import speedtest
from pythonping import ping

ipLocal = '192.168.0.1' 
localPingLim = 4 #miliseconds
speedInternet = 20
threshold = 0.85

def changeToMB(speed):
    return speed/1000000.0

print("Iniciando Teste de Velocidade da internet\n")
print("Testando conexão local, IP:{0}".format(ipLocal))


PingLocal = ping(ipLocal,count = 4,timeout=1)

if(PingLocal.rtt_avg_ms >= 4):
    print("\nPossivel PROBLEMA na conexao local, sugiro REINICIAR ROTEADOR")
    print("ping min/med/max: {0}/{1}/{2}  ms"
        .format(PingLocal.rtt_min_ms,PingLocal.rtt_avg_ms,PingLocal.rtt_max_ms))

else:
    print("\nConexao local SEM problemas, Resultado:")
    print("Ping min/med/max: {0}/{1}/{2}  ms"
        .format(PingLocal.rtt_min_ms,PingLocal.rtt_avg_ms,PingLocal.rtt_max_ms))
    
    print("\nIniciando teste no speedTest.net")

    servers = []
    # If you want to test against a specific server
    # servers = [1234]

    threads = None
    # If you want to use a single threaded test
    # threads = 1

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()

    results_dict = s.results.dict()
    #print(results_dict)
    
    if(results_dict['download'] >= (speedInternet*threshold)):
        print("Internet SEM problemas, caso ainda sinta lentidao REINICIE o PC")
    else:
        print("Internet COM problemas, procure sua operadora de internet")

    print("\nResultado:")
    print("Download: {:.2f}MB".format(changeToMB(results_dict['download'])))
    print("Upload: {:.2f}MB".format(changeToMB(results_dict['upload'])))
    print("Ping: {:.2f}ms".format(results_dict['ping']))
    print("")
    

    
