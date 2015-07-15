// Decompiled by Jad v1.5.8e. Copyright 2001 Pavel Kouznetsov.
// Jad home page: http://www.geocities.com/kpdus/jad.html
// Decompiler options: braces fieldsfirst space lnc 

package it.polictf2015;


public class b
{

    public static String a(String s)
    {
        return s.replace("c", "a");
    }

    public static String b(String s)
    {
        return s.replace("%", "");
    }

    public static String c(String s)
    {
        return s.replace("[", "");
    }

    public static String d(String s)
    {
        return s.replace("]", "");
    }

    public static String e(String s)
    {
        return s.replaceFirst("\\{", "");
    }

    public static String f(String s)
    {
        return s.replaceFirst("\\}", "");
    }

    public static String g(String s)
    {
        return s.replaceFirst("c", "f");
    }

    public static String h(String s)
    {
        return s.replaceFirst("R", "f");
    }

    public static String i(String s)
    {
        return s.replace("=", "_");
    }
}
