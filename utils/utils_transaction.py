from template.template_transaction import get_day, get_type, get_id, get_sum


def pt_all(l):
    print("All transactions \n")
    for x in l:
        print("Transaction with ID: " + str(get_id(x)))
        print("Day: " + str(get_day(x)) + " Sum: " +
              str(get_sum(x)) + " Type: " + str(get_type(x)))
        print("\n")


def pt_bigger(l, s):
    print("All transactions bigger than a given sum \n")
    for x in l:
        if get_sum(x) > s:
            print("Transaction with ID: " + str(get_id(x)))
            print("Day: " + str(get_day(x)) + " Sum: " +
                  str(get_sum(x)) + " Type: " + str(get_type(x)))
            print("\n")


def pt_untilday_bigger(l, day, s):
    print("All transactions made until the given date with the sum larger than the given number.\n")
    for x in l:
        if get_day(x) < day and get_sum(x) > s:
            print("Transaction with ID: " + str(get_id(x)))
            print("Day: " + str(get_day(x)) + " Sum: " +
                  str(get_sum(x)) + " Type: " + str(get_type(x)))
            print("\n")


def pt_type(l, tp):
    print("All transactions of a given type:\n")
    for x in l:
        if get_type(x) == tp:
            print("Transaction with ID: " + str(get_id(x)))
            print("Day: " + str(get_day(x)) + " Sum: " +
                  str(get_sum(x)) + " Type: " + str(get_type(x)))
            print("\n")


def dt_at_day(l, day):
    res = [x for x in l if (get_day(x) != day)]
    l[:] = res


def dt_at_period(l, ds, df):
    res = [x for x in l if not (get_day(x) >= ds and get_day(x) <= df)]
    l[:] = res


def dt_of_type(l, tp):
    res = [x for x in l if (get_type(x) != tp)]
    l[:] = res
