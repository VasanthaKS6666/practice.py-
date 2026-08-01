x = int("abc") / 0
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)
