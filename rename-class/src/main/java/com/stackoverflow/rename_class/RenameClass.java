package com.stackoverflow.rename_class;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.NodeList;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.Parameter;
import com.github.javaparser.utils.SourceRoot;

import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

/**
 * Rename generated classes using JavaParser.
 */
public class RenameClass {
    public static void main(String[] args) {
        Path path = Paths.get("./");
        SourceRoot sourceRootCSNIPPEX = new SourceRoot(path);
        SourceRoot sourceRootAPIZATOR = new SourceRoot(path);

        CompilationUnit cuCSNIPPEX = sourceRootCSNIPPEX.parse("", args[1]);
        CompilationUnit cuAPIZATOR = sourceRootAPIZATOR.parse("", args[0]);

        ArrayList<String> methodNames = new ArrayList<>();

        cuCSNIPPEX.findAll(MethodDeclaration.class).stream()
                .forEach(m -> {
                    methodNames.add(m.getNameAsString());
                });

        cuAPIZATOR.findAll(MethodDeclaration.class).stream()
                .forEach(m -> {
                    if (!methodNames.contains(m.getNameAsString())) {
                        m.setName("soEntry");
                        NodeList<Parameter> methodParameters = new NodeList<>();
                        m.getParameters().forEach(p -> {
                            methodParameters.add(p);
                        });
                        Collections.sort(methodParameters, new Comparator<Parameter>() {
                            @Override
                            public int compare(Parameter p1, Parameter p2) {
                                String p1Type = p1.getTypeAsString();
                                String p2Type = p2.getTypeAsString();
                                int typeCompare = p1Type.compareTo(p2Type);

                                if (typeCompare != 0) {
                                    return typeCompare;
                                }

                                String p1Name = p1.getNameAsString();
                                String p2Name = p2.getNameAsString();
                                return p1Name.compareTo(p2Name);
                            }
                        });
                        m.setParameters(methodParameters);
                    }
                });

        cuAPIZATOR.findAll(ClassOrInterfaceDeclaration.class).stream()
                .forEach(c -> {
                    if (c.getMethodsByName("soEntry").size() != 0) {

                        String classNameToChange = c.getNameAsString();
                        c.setName("SOClass");
                        String cuString = cuAPIZATOR.toString();
                        String newCUString = cuString.replace(classNameToChange, "SOClass");
                        try {
                            FileWriter fileWriter = new FileWriter(args[2] + "/SOClass.java");
                            fileWriter.write(newCUString);
                            fileWriter.close();
                            System.out.println("File created successfully.");
                        } catch (IOException e) {
                            System.out.println(e.getMessage());
                        }
                    }
                });
    }
}
