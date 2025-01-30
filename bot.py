import time
import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, ContextTypes, ChatJoinRequestHandler


load_dotenv()

# Get values from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
IMAGE_PATH = os.getenv("IMAGE_PATH")
PROMO_LINK = os.getenv("PROMO_LINK")

# Logging setup
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

# Function to approve join requests and send a message
async def approve_and_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("✅ Received a join request")  # Debugging

    request = update.chat_join_request  # Get join request details
    user_id = request.from_user.id
    user_name = request.from_user.first_name  # Get user name
    
    print(f"📌 User ID: {user_id}, Name: {user_name}")  # Debugging

    try:
        # Simulate 2-second delay for natural approval
        time.sleep(2)

        # Approve the join request
        await context.bot.approve_chat_join_request(CHANNEL_ID, user_id)
        logging.info(f"✅ Approved join request for {user_name} ({user_id})")
        print(f"📩 DM sent to: {user_id}")  # Debugging

        # Send a welcome message in private DM
        await context.bot.send_photo(
            chat_id=user_id,
            photo = IMAGE_PATH,
            caption=f"🎉Welcome {user_name} to the Ultimate Gaming Experience!🎉\n\n🚀 Get a MASSIVE 500% BONUS on your first deposit now! \n\n\Register in\n1win - {PROMO_LINK}\n\n🔥Use promo code: GET360🔥 \n\nDon't wait-grab your chance to WIN BIG today!💰 \n\nClaim your bonus now: Click Here {PROMO_LINK}✅"
        )
        logging.info(f"📩 Sent welcome message to {user_name} ({user_id})")
        print(f"📩 DM sent to: {user_id}")  # Debugging

    except Exception as e:
        logging.error(f"❌ Error approving user {user_id}: {e}")
        print(f"❌ Error: {e}")  # Debugging

# Main function to run the bot
def main():
    print("🚀 Bot is starting...")
    app = Application.builder().token(BOT_TOKEN).build()


    # Handler for approving join requests automatically
    app.add_handler(ChatJoinRequestHandler(approve_and_welcome))

    print("🤖 Bot is running and waiting for requests...")  # Debugging
    app.run_polling()

if __name__ == "__main__":
    main()