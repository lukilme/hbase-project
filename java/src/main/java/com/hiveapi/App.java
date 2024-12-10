package com.hiveapi;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class App {
    public static void main(String[] args) {
        String hiveUrl = "jdbc:hive2://localhost:10000/default"; 
        String user = "hive"; 
        String password = ""; 

        try {
          
            Class.forName("org.apache.hive.jdbc.HiveDriver");


            System.out.println("Conectanndo ao Hive...");
            Connection connection = DriverManager.getConnection(hiveUrl, user, password);
            System.out.println("Conexão estabelecida!");

            String createDatabaseQuery = "CREATE DATABASE IF NOT EXISTS java";
            executeQuery(connection, createDatabaseQuery);
            
            String useDatabaseQuery = "USE java";
            executeQuery(connection, useDatabaseQuery);
      
            String createTableQuery = "CREATE TABLE IF NOT EXISTS employees (id INT, name STRING, salary FLOAT) STORED AS TEXTFILE";
            executeQuery(connection, createTableQuery);

            String insertDataQuery = "INSERT INTO employees VALUES (1, 'John Doe', 50000.0)";
            executeQuery(connection, insertDataQuery);
         
            String selectQuery = "SELECT * FROM employees";
            try (
                Statement stmt = connection.createStatement(); 
                ResultSet rs = stmt.executeQuery(selectQuery)) {

                    System.out.println("Resultados da consulta:");
                    while (rs.next()) {
                        int id = rs.getInt("id");
                        String name = rs.getString("name");
                        float salary = rs.getFloat("salary");
                        System.out.printf("ID: %d, Nome: %s, Salário: %.2f%n", id, name, salary);
                    }
            }

            connection.close();
            System.out.println("Conexão encerrada.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void executeQuery(Connection connection, String query) throws Exception {
        try (Statement stmt = connection.createStatement()) {
            stmt.execute(query);
            System.out.println("Executado: " + query);
        }
    }
}
