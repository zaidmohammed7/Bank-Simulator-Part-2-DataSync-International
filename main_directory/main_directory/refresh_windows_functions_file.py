def signup_refresh_registry():
    from main_directory.SignupWindow import signup
    signup()


def login_refresh_registry():
    from main_directory.LoginWindow import login
    login()


def delete_refresh_registry():
    from main_directory.DeleteWindow import delete
    delete()


def home_refresh_registry():
    from main_directory.HomeWindow import home
    home()


def documentation_refresh_registry():
    from main_directory.DocumentationWindow import documentation
    documentation()


def account_window_refresh_registry(username, name):
    from main_directory.account_window import account_window
    account_window(username, name)


def del_win_refresh_registry(username, name, user_email):
    from main_directory.delete_confirm_window import del_confirm
    del_confirm(username, name, user_email)


def banking_wn_refresh_registry(name, card):
    from main_directory.banking_class import Banking
    bank_connect = Banking(name, card)
    bank_connect.mainloop()


def deposit_wn_refresh_registry(name, card):
    from main_directory.Deposit__reg__utils__ import Deposit
    deposit_wn_connect = Deposit(name, card)
    deposit_wn_connect.mainloop()


def refresh_chat__utils__():
    from main_directory.ChatBox__reg__utils__ import ChatApplicationWn
    app = ChatApplicationWn()
    app.run()


def refresh_pop_out_chat__utils__():
    from main_directory.PopOutChatBox__reg__utils__ import PopOutChatBox
    app = PopOutChatBox()
    app.run()


def refresh_currency_converter():
    from main_directory.CurrencyConverter__reg__utils__ import CurrencyConverter
    app = CurrencyConverter()
    app.run()


def refresh_calendar__utils__():
    from main_directory.Calendar__reg__utils__ import Calendar
    app = Calendar()
    app.run()


def refresh_pop_up_calendar__utils__():
    from main_directory.PopOutCalendar__reg__utils__ import PopOutCalendar
    app = PopOutCalendar()
    app.run()


def transfer_wn_refresh_registry(name, card):
    from main_directory.Transfer__reg__utils__ import TransferWn
    deposit_wn_connect = TransferWn(name, card)
    deposit_wn_connect.run()


def withdraw_wn_refresh_registry(name, card):
    from main_directory.Withdraw__reg__utils__ import WithdrawWn
    withdraw_wn_connect = WithdrawWn(name, card)
    withdraw_wn_connect.run()


def refresh_banking_calendar__utils__(name, card):
    from main_directory.Banking_Calendar__reg__sub__utils__ import BankingCalendar
    app = BankingCalendar(name, card)
    app.run()


def refresh_banking_pop_up_calendar__utils__(name, card):
    from main_directory.BankingPopOutCalendar__reg__sub__utils__ import BankingPopOutCalendar
    app = BankingPopOutCalendar(name, card)
    app.run()


def refresh_banking_chat_box__utils__(name, card):
    from main_directory.Banking_ChatBox__reg__sub__utils__ import BankingChatApplicationWn
    app = BankingChatApplicationWn(name, card)
    app.run()


def refresh_banking_pop_up_chat_box__utils__(name, card):
    from main_directory.BankingPopOutChatBox__reg__sub__utils__ import BankingPopOutChatBox
    app = BankingPopOutChatBox(name, card)
    app.run()


def refresh_change_password_window(username, name):
    from main_directory.account_wn_change_password__reg__utils__ import ChangePassword
    app = ChangePassword(username, name)
    app.run()


def refresh_change_pin_window(username, name):
    from main_directory.account_wn_change_pin__reg__utils__ import ChangePin
    app = ChangePin(username, name)
    app.run()


def refresh_phone_and_address_window(username, name):
    from main_directory.account_wn_change_phone_and_address__reg__utils__ import ChangePhoneAndAddress
    app = ChangePhoneAndAddress(username, name)
    app.run()


def refresh_admin_login():
    from main_directory.admin.admin_login import AdminLogin
    wn = AdminLogin()
    wn.run()


def refresh_admin_account(name):
    from main_directory.admin.admin_account import AdminAccount
    wn = AdminAccount(name)
    wn.run()
