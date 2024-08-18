import unittest
from trunco.daisy_ui.modal import (
    Modal,
    ModalBox,
    ModalAction,
    ModalBackdrop,
    ModalToggle,
    ModalPosition,
)
from trunco.components import ButtonComponent


class TestDaisyUIModal(unittest.TestCase):
    def test_modal_default(self):
        modal = Modal(
            content=[
                ModalBox(content=["This is the content of the modal"]),
                ModalAction(content=[ButtonComponent(label="Close")]),  # Fixed here
            ],
            position=ModalPosition.MIDDLE,
            is_open=True,
        )
        expected_html = (
            '<div id="{}" class="modal modal-middle modal-open">'
            '<div id="{}" class="modal-box">This is the content of the modal</div>'
            '<div id="{}" class="modal-action"><button id="{}" class="btn">Close</button></div>'
            "</div>"
        ).format(
            modal.id,
            modal.children[0].id,
            modal.children[1].id,
            modal.children[1].children[0].id,
        )
        self.assertEqual(str(modal), expected_html)

    def test_modal_with_backdrop(self):
        modal = Modal(
            content=[
                ModalBackdrop(),
                ModalBox(content=["This is the content of the modal"]),
            ],
            position=ModalPosition.BOTTOM,
        )
        expected_html = (
            '<div id="{}" class="modal modal-bottom">'
            '<label id="{}" class="modal-backdrop"></label>'
            '<div id="{}" class="modal-box">This is the content of the modal</div>'
            "</div>"
        ).format(modal.id, modal.children[0].id, modal.children[1].id)
        self.assertEqual(str(modal), expected_html)

    def test_modal_with_toggle(self):
        toggle_id = "modal-toggle-id"
        modal_toggle = ModalToggle(target_id=toggle_id)
        modal = Modal(
            content=[
                modal_toggle,
                ModalBox(content=["This is the content of the modal"]),
            ],
            position=ModalPosition.TOP,
        )
        expected_html = (
            '<div id="{}" class="modal modal-top">'
            '<input id="modal-toggle-id" class="modal-toggle" type="checkbox">'
            '<div id="{}" class="modal-box">This is the content of the modal</div>'
            "</div>"
        ).format(modal.id, modal.children[1].id)
        self.assertEqual(str(modal), expected_html)


if __name__ == "__main__":
    unittest.main()
