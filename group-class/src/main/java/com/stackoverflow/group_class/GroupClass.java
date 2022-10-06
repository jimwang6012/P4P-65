package com.stackoverflow.group_class;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.utils.SourceRoot;
import org.apache.commons.io.FileUtils;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;

/**
 * Rename generated classes using JavaParser.
 */
public class GroupClass {
    public static void main(String[] args) throws IOException {
        File dir = new File(args[0]);

        LinkedHashMap<ArrayList<String>, ArrayList<String>> classGroups = new LinkedHashMap<>();

        for (File file : dir.listFiles()) {
            if (!file.equals(new File(dir + "/groups"))) {
                Path path = Paths.get(file + "/com/stackoverflow/api/");

                SourceRoot sourceRoot = new SourceRoot(path);
                CompilationUnit cu = sourceRoot.parse("", "SOClass.java");

                cu.findAll(MethodDeclaration.class).stream()
                        .forEach(m -> {
                            if (m.getNameAsString().equals("soEntry")) {
                                ArrayList<String> parameterTypes = new ArrayList<>();
                                ArrayList<String> parameterNames = new ArrayList<>();

                                m.getParameters().forEach(p -> {
                                    parameterTypes.add(p.getTypeAsString());
                                    parameterNames.add(p.getNameAsString());
                                });

                                if (classGroups.size() == 0) {
                                    ArrayList<String> classGroup = new ArrayList<>();
                                    classGroup.add(parameterTypes.toString());
                                    classGroup.add(parameterNames.toString());
                                    ArrayList<String> classesInGroup = new ArrayList<>();
                                    classesInGroup.add(file.toString());
                                    classGroups.put(classGroup, classesInGroup);
                                } else {
                                    ArrayList<ArrayList<String>> classGroupKeys = new ArrayList<>(classGroups.keySet());
                                    boolean isFound = false;
                                    for (int i = 0; i < classGroupKeys.size(); i++) {
                                        String typeString = classGroupKeys.get(i).get(0);
                                        String nameString = classGroupKeys.get(i).get(1);
                                        if (typeString.equals(parameterTypes.toString())) {
                                            if (nameString.equals(parameterNames.toString())) {
                                                classGroups.get(classGroupKeys.get(i)).add(file.toString());
                                                isFound = true;
                                            } else {
                                                boolean isSameGroup = true;
                                                ArrayList<String> types = new ArrayList<>(Arrays.asList(typeString.substring(1, typeString.length() - 1).split(", ")));
                                                ArrayList<String> names = new ArrayList<>(Arrays.asList(nameString.substring(1, nameString.length() - 1).split(", ")));

                                                for (int j = 1; j < types.size(); j++) {
                                                    if (types.get(j).equals(types.get(j - 1))) {
                                                        if (!names.get(j).equals(names.get(j - 1))) {
                                                            isSameGroup = false;
                                                        }
                                                    }
                                                }

                                                if (isSameGroup) {
                                                    classGroups.get(classGroupKeys.get(i)).add(file.toString());
                                                    isFound = true;
                                                }
                                            }
                                        }
                                    }
                                    if (!isFound) {
                                        ArrayList<String> classGroup = new ArrayList<>();
                                        classGroup.add(parameterTypes.toString());
                                        classGroup.add(parameterNames.toString());
                                        ArrayList<String> classesInGroup = new ArrayList<>();
                                        classesInGroup.add(file.toString());
                                        classGroups.put(classGroup, classesInGroup);
                                    }
                                }
                            }
                        });
            }
        }

        int num = 1;
        for (ArrayList<String> answerIds : classGroups.values()) {
            File targetFile = new File(args[0] + "/groups/group-" + num);
            targetFile.getParentFile().mkdirs();
            for (String answerId : answerIds) {
                FileUtils.copyDirectoryToDirectory(new File(answerId), targetFile);
            }
            num++;
        }
    }
}
