$(document).ready(function() {
    $('#participants').DataTable();
} );

var backend_url = "127.0.0.1:8000/"

function hideOtherSections(ids) {
	ids.forEach(id => {
		let element = document.getElementById(id);
		element.style.display = "none";
	});
}
function displayTasks(id) {
	let element = document.getElementById(id);
	element.style.display = "block";
	const sections = ["participant-table", "connection-table", "invite-table", "recording-table"]
	hideOtherSections(sections)
}

function displayParticipantTable(id) {
	let element = document.getElementById(id);
	element.style.display = "block";
	const sections = ["tasks", "connection-table", "invite-table", "recording-table"]
	hideOtherSections(sections)
}

function displayConnectionsTable(id) {
	let element = document.getElementById(id);
	element.style.display = "block";
	const sections = ["tasks", "participant-table", "invite-table", "recording-table"]
	hideOtherSections(sections)
}

function displayInviteTable(id) {
	let element = document.getElementById(id);
	element.style.display = "block";
	const sections = ["tasks", "participant-table", "connection-table", "recording-table"]
	hideOtherSections(sections)
}

function displayRecordingTable(id) {
	let element = document.getElementById(id);
	element.style.display = "block";

	const sections = ["tasks", "participant-table", "connection-table", "invite-table"]
	hideOtherSections(sections)
}

function toggle_add_task_modal(id) {
	$('#'+id).modal('show') 
}

function close_add_task_modal(id) {
	$('#'+id).modal('hide') 
}

function toggle_add_participant_modal(id) {
	$('#'+id).modal('show')
}

function close_add_participant_modal(id) {
	$('#'+id).modal('hide')
}

function toggle_edit_task_modal(id, task_id, task_title, task_description) {
	$('#'+id).modal('show')

	let title = document.querySelector("#edit-task-form #task-title");
	title.value = task_title

	let description = document.querySelector("#edit-task-form #task-description");
	description.value = task_description

	let task_id_elem = document.querySelector("#edit-task-form #task-id");
	task_id_elem.value = task_id;
	task_id_elem.readOnly = true;
}

function toggle_add_connection_modal(id) {
	$('#'+id).modal('show')
}

function close_add_connection_modal(id) {
	$('#'+id).modal('hide')
}

function close_add_recording_modal(id) {
	$('#'+id).modal('hide')
}

function open_record_task_modal(id, participant_id, task_id) {
	$('#'+id).modal('show')

	let element = document.getElementById('hidden-task-id');

	element.innerHTML = task_id;

	element = document.getElementById('hidden-participant-id')

	element.innerHTML = participant_id;
}

function close_record_task_modal(id) {
	$('#'+id).modal('hide')
}