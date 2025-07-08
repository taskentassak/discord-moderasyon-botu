import discord
from discord.ext import commands
import os
import json
import asyncio
from datetime import datetime
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# Import command modules
from commands.moderation import ModerationCommands
from commands.messaging import MessagingCommands
from commands.server_management import ServerManagementCommands
from config.settings import BOT_CONFIG

# Bot setup with intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=BOT_CONFIG['PREFIX'], intents=intents, help_command=None)

@bot.event
async def on_ready():
    """Bot başlatıldığında çalışır"""
    print(f'{bot.user} olarak giriş yapıldı!')
    print(f'Bot {len(bot.guilds)} sunucuda aktif.')
    
    # Set bot activity
    activity = discord.Game(name=f"{BOT_CONFIG['PREFIX']}yardım | Moderasyon Botu")
    await bot.change_presence(activity=activity)

@bot.event
async def on_command_error(ctx, error):
    """Hata yönetimi"""
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="❌ Yetki Hatası",
            description="Bu komutu kullanmak için gerekli yetkilere sahip değilsiniz.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title="❌ Komut Bulunamadı",
            description="Geçersiz komut. Komut listesi için `.yardım` yazın.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="❌ Eksik Parametre",
            description="Komut için gerekli parametreleri girmediniz.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="❌ Hata",
            description=f"Bir hata oluştu: {str(error)}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

@bot.command(name='yardım', aliases=['help', 'komutlar'])
async def help_command(ctx):
    """Yardım komutu"""
    embed = discord.Embed(
        title="🤖 Bot Komutları",
        description="Tüm komutların listesi:",
        color=discord.Color.blue()
    )
    
    # Moderation commands
    embed.add_field(
        name="🛡️ Moderasyon",
        value=f"`{BOT_CONFIG['PREFIX']}ban <kullanıcı> [sebep]`\n"
              f"`{BOT_CONFIG['PREFIX']}unban <kullanıcı_id>`\n"
              f"`{BOT_CONFIG['PREFIX']}kick <kullanıcı> [sebep]`\n"
              f"`{BOT_CONFIG['PREFIX']}mute <kullanıcı> [süre] [sebep]`\n"
              f"`{BOT_CONFIG['PREFIX']}unmute <kullanıcı>`",
        inline=False
    )
    
    # Messaging commands
    embed.add_field(
        name="💬 Mesajlaşma",
        value=f"`{BOT_CONFIG['PREFIX']}yaz <kanal> <mesaj>`\n"
              f"`{BOT_CONFIG['PREFIX']}herkeseyaz <mesaj>`",
        inline=False
    )
    
    # Server management commands
    embed.add_field(
        name="⚙️ Sunucu Yönetimi (Sadece Kurucu)",
        value=f"`{BOT_CONFIG['PREFIX']}imha`\n"
              f"`{BOT_CONFIG['PREFIX']}gerigetir`",
        inline=False
    )
    
    embed.set_footer(text=f"Komut prefixi: {BOT_CONFIG['PREFIX']}")
    await ctx.send(embed=embed)

# Add cogs
async def setup_cogs():
    """Cog'ları ekle"""
    await bot.add_cog(ModerationCommands(bot))
    await bot.add_cog(MessagingCommands(bot))
    await bot.add_cog(ServerManagementCommands(bot))

async def main():
    """Ana fonksiyon"""
    # Bot token'ını environment variable'dan veya varsayılan olarak al
    token = os.getenv('DISCORD_TOKEN', 'MTM5MTkwNDM2ODEwMTQyOTM2OQ.GDYdBp.fCjL82UwFkdMA0mNwr2yk-3-UkT56GH2nubTPI')
    
    # Cog'ları yükle
    await setup_cogs()
    
    # Botu başlat
    await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
