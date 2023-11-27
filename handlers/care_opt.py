from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

from handlers.status import User_Status
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from keyboards.for_opt import select_opt_option
from keyboards.for_questions import get_retail_or_wholesale
from keyboards.for_retail import select_retail_option
from keyboards.restart_menu import get_restart_menu
from keyboards.for_care import select_care

router = Router()  # [1]


@router.message(User_Status.selected_care_by_opt, F.text.lower() == "подушки")
async def select_podushki(message: Message, state: FSMContext):
    album_builder = MediaGroupBuilder()
    album_builder.add(
        type="photo",
        media=FSInputFile("resources/podushki.jpg")
    )
    await message.answer_media_group(
        media=album_builder.build()
    )
    await message.answer(
        text="<b>Инструкция по уходу за подушками</b>\n\n"
             "Перед эксплуатацией подушку нужно взбить в течении трёх минут для равномерного распределения волокна,"
             "а так же ежедневно взбивать после пробуждения.При этом слежавшийся за ночь наполнитель приобретает рыхлость и проветривается."
             "Подушку нужно регулярно, желательно раз в неделю, проветривать на свежем воздухе.\n"
             "Желательно также просушивать ее на теплом воздухе, но не под прямыми солнечными лучами.\n"
             "Хранение можно осушествлять в обычной простыне, при отсутствии специального чехла.\n"
             "Не хранить в полиэтиленовых пакетах.\n"
             "Все изделия рекомендовано чистить в строгом соответствии символам на ярлыке.",
        reply_markup=get_restart_menu(),
        parse_mode=ParseMode.HTML
    )
    await state.set_state(User_Status.end_care_by_opt)


@router.message(User_Status.selected_care_by_opt, F.text.lower() == "одеяла")
async def select_odeiala(message: Message, state: FSMContext):
    album_builder = MediaGroupBuilder()
    album_builder.add(
        type="photo",
        media=FSInputFile("resources/odeiala.jpg")
    )
    await message.answer_media_group(
        media=album_builder.build()
    )
    await message.answer(
        text="<b>Инструкция по уходу за одеялами</b>\n\n"
             "Перед эксплуатацией одеяло нужно стряхнуть для равномерного распределения волокна, а так же ежедневно стряхивать после пробуждения.\n"
             "При этом слежавшийся за ночь наполнитель приобретает рыхлость и проветривается.\n"
             "Одеяло нужно регулярно, желательно раз в неделю, проветривать на свежем воздухе.\n"
             "Желательно также просушивать его на теплом воздухе, но не под прямыми солнечными лучами.\n"
             "Хранение можно осуществлять в обычной простыне, при отсутствии специального чехла.\n"
             "Не хранить в полиэтиленовых пакетах.\n"
             "Важно одевать на одеяло пододеяльник.\n"
             "Все изделия рекомендовано чистить в строгом соответствии символам на ярлыке.\n",
        reply_markup=get_restart_menu(),
        parse_mode=ParseMode.HTML
    )
    await state.set_state(User_Status.end_care_by_opt)


@router.message(User_Status.selected_care_by_opt, F.text.lower() == "наматрацники")
async def select_namatracniki(message: Message, state: FSMContext):
    album_builder = MediaGroupBuilder()
    album_builder.add(
        type="photo",
        media=FSInputFile("resources/namatracniki.jpg")
    )
    await message.answer_media_group(
        media=album_builder.build()
    )
    await message.answer(
        text="<b>Инструкция по уходу за наматрацниками</b>\n\n"
             "Если наполнитель слегка свалялся (при его наличии) в процессе использования, то перед стиркой его нужно распрямить.\n"
             "Наматрацники не нужно стирать слишком часто, как постельное белье. Стирка рекомендована раз в 3-6 месяцев. Раз в месяц их необходимо проветривать, а раз в неделю\n"
             "- пылесосить со специальной насадкой для мебели с мягким ворсом (не путать с щеткой для ковра, чьи грубые щетинки могут оставить зацепки на трикотажной или махровой ткани). Можно выбивать наматрацник вручную.\n"
             "Хранение можно осуществлять в обычной простыне, при отсутствии специального чехла. Не хранить в полиэтиленовых пакетах.\n"
             "Все изделия рекомендовано чистить в строгом соответствии символам на ярлыке.\n",
        reply_markup=get_restart_menu(),
        parse_mode=ParseMode.HTML
    )
    await state.set_state(User_Status.end_care_by_opt)

