// Decompiled by Jad v1.5.8e. Copyright 2001 Pavel Kouznetsov.
// Jad home page: http://www.geocities.com/kpdus/jad.html
// Decompiler options: braces fieldsfirst space lnc 

package it.polictf2015;

import android.app.Activity;
import android.content.Context;
import android.content.Loader;
import android.database.Cursor;
import android.os.Bundle;
import android.telephony.TelephonyManager;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

// Referenced classes of package it.polictf2015:
//            c, b, a

public class LoginActivity extends Activity
    implements android.app.LoaderManager.LoaderCallbacks
{

    private EditText a;
    private View b;

    public LoginActivity()
    {
    }

    private void a()
    {
        EditText edittext = null;
        a.setError(null);
        String s = a.getText().toString();
        boolean flag = false;
        if (TextUtils.isEmpty(s))
        {
            a.setError(getString(0x7f0c003b));
            edittext = a;
            flag = true;
        }
        EditText edittext1 = edittext;
        boolean flag1 = flag;
        if (!TextUtils.isEmpty(s))
        {
            edittext1 = edittext;
            flag1 = flag;
            if (!a(s))
            {
                a.setError(getString(0x7f0c0037));
                edittext1 = a;
                flag1 = true;
            }
        }
        if (flag1)
        {
            edittext1.requestFocus();
        }
    }

    static void a(LoginActivity loginactivity)
    {
        loginactivity.a();
    }

    private boolean a(Context context, double d)
    {
        if (d == 3.4100000000000001D);
        return ((TelephonyManager)context.getSystemService("phone")).getSubscriberId().equalsIgnoreCase("310260000000000");
    }

    private boolean a(Context context, int i)
    {
        if (i == 2);
        return ((TelephonyManager)context.getSystemService("phone")).getNetworkOperatorName().equalsIgnoreCase("android");
    }

    private boolean a(Context context, String s)
    {
        s.replace("flagging", "flag");
        return ((TelephonyManager)context.getSystemService("phone")).getLine1Number().startsWith("1555521");
    }

    private boolean a(Context context, boolean flag)
    {
        context = ((TelephonyManager)context.getSystemService("phone")).getDeviceId();
        return context.equalsIgnoreCase("000000000000000") || context.equalsIgnoreCase("012345678912345") || context.equalsIgnoreCase("e21833235b6eef10");
    }

    private boolean a(String s)
    {
        if (s.equals(c.a(it.polictf2015.b.a(it.polictf2015.b.b(it.polictf2015.b.c(it.polictf2015.b.d(it.polictf2015.b.g(it.polictf2015.b.h(it.polictf2015.b.e(it.polictf2015.b.f(it.polictf2015.b.i(c.c(c.b(c.d(getString(0x7f0c0038))))))))))))))))
        {
            Toast.makeText(getApplicationContext(), getString(0x7f0c003c), 1).show();
            return true;
        } else
        {
            return false;
        }
    }

    public void a(Loader loader, Cursor cursor)
    {
    }

    protected void onCreate(Bundle bundle)
    {
        super.onCreate(bundle);
        setContentView(0x7f040017);
        if (a(getApplicationContext(), 2) || a(getApplicationContext(), "flagging{It_cannot_be_easier_than_this}") || a(getApplicationContext(), false) || a(getApplicationContext(), 2.7799999999999998D))
        {
            Toast.makeText(getApplicationContext(), getString(0x7f0c003d), 1).show();
        } else
        {
            Toast.makeText(getApplicationContext(), getString(0x7f0c003a), 1).show();
        }
        a = (EditText)findViewById(0x7f0a0055);
        ((Button)findViewById(0x7f0a0056)).setOnClickListener(new a(this));
        b = findViewById(0x7f0a0053);
    }

    public Loader onCreateLoader(int i, Bundle bundle)
    {
        return null;
    }

    public void onLoadFinished(Loader loader, Object obj)
    {
        a(loader, (Cursor)obj);
    }

    public void onLoaderReset(Loader loader)
    {
    }
}
