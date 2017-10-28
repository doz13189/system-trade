from apscheduler.schedulers.blocking import BlockingScheduler
import trade_bitcoin


scheduler = BlockingScheduler()

trade_bitcoin.hello()

for h in range(24):
	m = 1
	for i in range(12):
		scheduler.add_job(trade_bitcoin.trade, "cron", hour=h, minute=m)
		m += 5

	scheduler.add_job(trade_bitcoin.settlement, "cron", hour=h, minute=58)

scheduler.start()
