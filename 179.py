



def llay_bank_account():
    account_state = str(input())
    is_negative = int(account_state) < 0

    if not is_negative:
        print(account_state)
        return

    last = int(account_state[:-1])
    before_last = int(account_state[:-2] + account_state[-1]) 

    print(max(last, before_last))

llay_bank_account()