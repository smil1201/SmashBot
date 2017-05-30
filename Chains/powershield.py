import melee
import globals
from melee.enums import Action, Button
from Chains.chain import Chain

class Powershield(Chain):
    def step(self):
        controller = globals.controller
        smashbot_state = globals.smashbot_state

        isshielding = smashbot_state.action == Action.SHIELD \
            or smashbot_state.action == Action.SHIELD_START \
            or smashbot_state.action == Action.SHIELD_REFLECT \
            or smashbot_state.action == Action.SHIELD_STUN \
            or smashbot_state.action == Action.SHIELD_RELEASE

        # If we're in shield stun, we can let go
        if smashbot_state.action == Action.SHIELD_STUN:
            interruptible = True
            controller.empty_input()
            return

        # If we already pressed L last frame, let go
        if controller.prev.button[Button.BUTTON_L]:
            controller.empty_input()
            return

        if not isshielding:
            interruptible = False
            controller.press_button(Button.BUTTON_L);
            return

        interruptible = True
        controller.empty_input()
