extends Area2D

@onready var timer: Timer = $Timer


func _on_body_entered(body):
	print("Aaaa...")
	if body.has_method("die"):
		body.die()
	timer.start()


func _on_timer_timeout():
	get_tree().reload_current_scene()
