package com.hiveapi;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.TableName;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.util.Bytes;


public class App {
    public static void main( String[] args )
    {
        try {
            // Configuração do HBase
            Configuration config = HBaseConfiguration.create();
            config.set("hbase.zookeeper.quorum", "localhost"); // Host do ZooKeeper
            config.set("hbase.zookeeper.property.clientPort", "2181"); // Porta do ZooKeeper

            // Estabelecendo conexão
            System.out.println("Conectando ao HBase...");
            Connection connection = ConnectionFactory.createConnection(config);
            System.out.println("Conexão estabelecida!");

            // Fechando a conexão
            connection.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
