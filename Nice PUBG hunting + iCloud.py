from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
import random
import time
from pyfiglet import Figlet
from colorama import init, Fore, Style
import string
import webbrowser

url = "https://t.me/XSromz"
webbrowser.open(url)

"""
By Vermouth7 
Tele: @Isk_x
INSTA  @m3.a0
"""
init(autoreset=True)

console = Console()

domains = ["gmail.com", "icloud.com"]

def generate_random_email():
    domain = random.choice(domains)
    username = f"user{random.randint(1000, 9999)}"
    return f"{username}@{domain}"

def generate_random_password():
    password_length = random.randint(8, 12)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(password_length))

def generate_random_player_id():
    return ''.join(random.choice(string.digits) for _ in range(10))

def display_account_info(email, password, country, player_id, level):
    table = Table(title="PUBG Account Information")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="magenta")
    table.add_row("Email", email)
    table.add_row("Password", password)
    table.add_row("Country", country)
    table.add_row("Player ID", player_id)
    table.add_row("Level", str(level))
    console.print(Panel(table, title="[bold green]Account caught![/bold green]"))

def catch_pubg_account():
    console.print(Panel("[bold yellow]Starting PUBG Account Hunter...[/bold yellow]", border_style="blue"))

    while True:
        chance = random.random()  # Scor id

        if chance < 0.05:  # 5% chance of catching an account
            email = generate_random_email()
            password = generate_random_password()
            country = "Iraq"
            player_id = generate_random_player_id()
            level = random.randint(1, 75)

            display_account_info(email, password, country, player_id, level)

            # Simulate CAPTCHA verification
            console.print("[yellow]Please verify CAPTCHA to continue.[/yellow]")
            captcha_link = f"https://pubg.com/verify?captcha=PUBG&player_id={player_id}&email={email}"
            console.print(f"[blue]CAPTCHA verification link: {captcha_link}[/blue]")
            time.sleep(5)  # Simulate time taken to verify CAPTCHA
            console.print("[green]CAPTCHA verified successfully![/green]")
        
        else:
            console.print(Panel("[red]No account caught this time.[/red]", border_style="red"))

        time.sleep(1)

if __name__ == "__main__":
    fig = Figlet(font='slant')
    print(Fore.GREEN + fig.renderText('Vermouth'))
    print(Fore.RED + """     PUBG account hunting\n
       By Vermouth7 
         Tele: @Isk_x
            INSTA  @m3.a0
""")
    catch_pubg_account()
